'use client';

import { motion } from 'framer-motion';
import { Target, Shield, Globe } from 'lucide-react';

export default function Approach() {
  return (
    <section className="py-24 bg-[#002B49] text-white overflow-hidden relative" id="approach">
      {/* Background patterns */}
      <div className="absolute top-0 left-0 w-full h-full z-0 opacity-10">
        <div className="absolute top-0 right-0 w-1/2 h-full bg-gradient-to-l from-teal-900 to-transparent"></div>
        <div className="grid grid-cols-12 grid-rows-12 gap-4 w-full h-full transform rotate-12 scale-150">
          {[...Array(20)].map((_, i) => (
             <div key={i} className="bg-white/5 rounded-full w-2 h-2"></div>
          ))}
        </div>
      </div>

      <div className="container mx-auto px-6 relative z-10">
        <div className="flex flex-col md:flex-row justify-between items-end mb-16 gap-8">
          <div className="md:w-1/2">
            <span className="text-teal-400 font-semibold tracking-wider text-sm uppercase">Vision Stratégique</span>
            <h2 className="text-4xl md:text-5xl font-extrabold mt-2 mb-6 leading-tight">L&apos;Approche Galilée</h2>
            <p className="text-gray-300 text-lg leading-relaxed">
              Nous ne cherchons pas seulement la rentabilité, mais la souveraineté. Notre thèse d&apos;investissement repose sur la création d&apos;infrastructures technologiques critiques pour l&apos;Afrique.
            </p>
          </div>

          <div className="md:w-1/2 flex justify-between items-center gap-4 text-center">
             <div>
                <div className="text-4xl md:text-5xl font-bold text-white mb-1">24/7</div>
                <div className="text-teal-500 text-xs font-bold uppercase tracking-wider">Mentorat Actif</div>
             </div>
             <div className="w-px h-12 bg-white/20"></div>
             <div>
                <div className="text-4xl md:text-5xl font-bold text-white mb-1">3x</div>
                <div className="text-teal-500 text-xs font-bold uppercase tracking-wider">Croissance Annuelle</div>
             </div>
             <div className="w-px h-12 bg-white/20"></div>
             <div>
                <div className="text-4xl md:text-5xl font-bold text-white mb-1">100%</div>
                <div className="text-teal-500 text-xs font-bold uppercase tracking-wider">Souveraineté</div>
             </div>
          </div>
        </div>

        <div className="grid grid-cols-1 md:grid-cols-3 gap-8 border-t border-white/10 pt-16">
          <motion.div
             className="group"
             whileHover={{ y: -5 }}
             transition={{ duration: 0.3 }}
          >
            <div className="w-12 h-12 bg-teal-500/20 rounded-lg flex items-center justify-center mb-6 group-hover:bg-teal-500 transition-colors duration-300">
               <Target className="text-teal-400 group-hover:text-white" />
            </div>
            <h3 className="text-xl font-bold mb-3 group-hover:text-teal-400 transition-colors">Deal-Flow Qualifié</h3>
            <p className="text-gray-400 text-sm leading-relaxed">
               Accès exclusif aux startups les plus prometteuses, pré-validées par notre studio technique.
            </p>
          </motion.div>

          <motion.div
             className="group"
             whileHover={{ y: -5 }}
             transition={{ duration: 0.3 }}
          >
            <div className="w-12 h-12 bg-teal-500/20 rounded-lg flex items-center justify-center mb-6 group-hover:bg-teal-500 transition-colors duration-300">
               <Shield className="text-teal-400 group-hover:text-white" />
            </div>
            <h3 className="text-xl font-bold mb-3 group-hover:text-teal-400 transition-colors">De-Risking</h3>
            <p className="text-gray-400 text-sm leading-relaxed">
               Notre accompagnement opérationnel réduit drastiquement le taux d&apos;échec des startups en portefeuille.
            </p>
          </motion.div>

          <motion.div
             className="group"
             whileHover={{ y: -5 }}
             transition={{ duration: 0.3 }}
          >
            <div className="w-12 h-12 bg-teal-500/20 rounded-lg flex items-center justify-center mb-6 group-hover:bg-teal-500 transition-colors duration-300">
               <Globe className="text-teal-400 group-hover:text-white" />
            </div>
            <h3 className="text-xl font-bold mb-3 group-hover:text-teal-400 transition-colors">Impact Pan-Africain</h3>
            <p className="text-gray-400 text-sm leading-relaxed">
               Investissez dans des solutions qui résolvent des problèmes structurels à l&apos;échelle du continent.
            </p>
          </motion.div>
        </div>
      </div>
    </section>
  );
}
