from models.portfolio import PortfolioProject
from models import db
from services.file_service import save_file

class PortfolioService:
    @staticmethod
    def get_all_projects(active_only=False):
        """
        Retrieves all portfolio projects, optionally filtering by active status.
        Ordered by creation date descending.
        """
        query = PortfolioProject.query
        if active_only:
            query = query.filter_by(is_active=True)
        return query.order_by(PortfolioProject.created_at.desc()).all()

    @staticmethod
    def get_project_by_id(project_id):
        """
        Retrieves a single project by ID or 404s.
        """
        return PortfolioProject.query.get_or_404(project_id)

    @staticmethod
    def create_project(data, file=None):
        """
        Creates a new portfolio project with the provided data and optional image file.
        """
        title = data.get('title')
        category = data.get('category')
        description = data.get('description')
        project_url = data.get('project_url')
        is_active = True if data.get('is_active') else False

        image_url = None
        if file:
            filename = save_file(file, subfolder='portfolio')
            if filename:
                image_url = f"uploads/portfolio/{filename}"

        new_project = PortfolioProject(
            title=title,
            category=category,
            description=description,
            project_url=project_url,
            is_active=is_active,
            image_url=image_url
        )
        db.session.add(new_project)
        db.session.commit()
        return new_project

    @staticmethod
    def update_project(project_id, data, file=None):
        """
        Updates an existing project. Handles file replacement if a new file is provided.
        """
        project = PortfolioProject.query.get_or_404(project_id)

        project.title = data.get('title')
        project.category = data.get('category')
        project.description = data.get('description')
        project.project_url = data.get('project_url')
        project.is_active = True if data.get('is_active') else False

        if file:
            filename = save_file(file, subfolder='portfolio')
            if filename:
                project.image_url = f"uploads/portfolio/{filename}"

        db.session.commit()
        return project

    @staticmethod
    def delete_project(project_id):
        """
        Deletes a project by ID.
        """
        project = PortfolioProject.query.get_or_404(project_id)
        db.session.delete(project)
        db.session.commit()
        return True
