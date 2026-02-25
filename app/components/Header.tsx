'use client';

import Link from 'next/link';
import { Menu, X } from 'lucide-react';
import { useState } from 'react';

export default function Header() {
  const [isOpen, setIsOpen] = useState(false);

  return (
    <header className="sticky top-0 z-50 bg-white shadow-sm border-b border-gray-100">
      <div className="container mx-auto px-6 py-4 flex justify-between items-center">
        {/* Logo */}
        <Link href="/" className="flex items-center gap-2">
          <div className="text-2xl font-bold text-[#002B49]">
            Shabaka <span className="font-light">InnovLab</span>
          </div>
        </Link>

        {/* Desktop Navigation */}
        <nav className="hidden md:flex items-center gap-8">
          <Link href="#parcours" className="text-gray-600 hover:text-[#002B49] font-medium transition-colors">
            Parcours
          </Link>
          <Link href="#solutions" className="text-gray-600 hover:text-[#002B49] font-medium transition-colors">
            Solutions B2B
          </Link>
          <Link href="#investisseurs" className="text-gray-600 hover:text-[#002B49] font-medium transition-colors">
            Investisseurs
          </Link>
        </nav>

        {/* CTA Button */}
        <div className="hidden md:block">
          <Link
            href="#join"
            className="bg-[#006D77] hover:bg-[#005a63] text-white px-6 py-2.5 rounded-lg font-medium transition-colors shadow-lg hover:shadow-xl transform hover:-translate-y-0.5 duration-200"
          >
            Rejoindre l&apos;aventure
          </Link>
        </div>

        {/* Mobile Menu Button */}
        <button
          className="md:hidden text-gray-700"
          onClick={() => setIsOpen(!isOpen)}
        >
          {isOpen ? <X size={28} /> : <Menu size={28} />}
        </button>
      </div>

      {/* Mobile Menu */}
      {isOpen && (
        <div className="md:hidden bg-white border-t border-gray-100 py-4 px-6 flex flex-col gap-4 shadow-lg absolute w-full left-0">
          <Link
            href="#parcours"
            className="text-gray-600 hover:text-[#002B49] font-medium py-2"
            onClick={() => setIsOpen(false)}
          >
            Parcours
          </Link>
          <Link
            href="#solutions"
            className="text-gray-600 hover:text-[#002B49] font-medium py-2"
            onClick={() => setIsOpen(false)}
          >
            Solutions B2B
          </Link>
          <Link
            href="#investisseurs"
            className="text-gray-600 hover:text-[#002B49] font-medium py-2"
            onClick={() => setIsOpen(false)}
          >
            Investisseurs
          </Link>
          <Link
            href="#join"
            className="bg-[#006D77] hover:bg-[#005a63] text-white px-6 py-2.5 rounded-lg font-medium text-center"
            onClick={() => setIsOpen(false)}
          >
            Rejoindre l&apos;aventure
          </Link>
        </div>
      )}
    </header>
  );
}
