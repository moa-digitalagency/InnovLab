'use client';

import Link from 'next/link';
import { Mail, Phone, MapPin, Send } from 'lucide-react';

export default function Footer() {
  return (
    <footer className="bg-[#001d31] text-white pt-20 pb-10" id="contact">
      <div className="container mx-auto px-6">
        <div className="grid grid-cols-1 md:grid-cols-4 gap-12 border-b border-gray-800 pb-16">

          {/* Logo and About */}
          <div>
            <div className="text-2xl font-bold text-white mb-6">
              Shabaka <span className="font-light text-teal-400">InnovLab</span>
            </div>
            <p className="text-gray-400 text-sm mb-8 leading-relaxed">
              Le point de convergence de l&apos;innovation, du capital et de l&apos;industrie pour une Afrique souveraine.
            </p>
            <div className="flex gap-2">
              <input
                type="email"
                placeholder="Votre email"
                className="bg-[#002B49] border border-gray-700 rounded-lg px-4 py-2 text-sm focus:outline-none focus:border-teal-500 flex-grow"
              />
              <button className="bg-teal-600 hover:bg-teal-500 p-2 rounded-lg transition-colors">
                <Send size={18} />
              </button>
            </div>
          </div>

          {/* Contact Direct */}
          <div>
            <h4 className="font-bold text-lg mb-6">Contact Direct</h4>
            <ul className="space-y-4 text-sm text-gray-400">
              <li className="flex items-start gap-3">
                <MapPin className="text-teal-500 w-5 h-5 flex-shrink-0" />
                <span>Centre d&apos;affaires Guéliz, Bd My Rachid, Étage 1, Bureau 8, 40000 Marrakech</span>
              </li>
              <li className="flex items-center gap-3">
                <Phone className="text-teal-500 w-5 h-5 flex-shrink-0" />
                <span>+212 699 14 09 61</span>
              </li>
              <li className="flex items-center gap-3">
                <Mail className="text-teal-500 w-5 h-5 flex-shrink-0" />
                <a href="mailto:re@shabaka.io" className="hover:text-white transition-colors">re@shabaka.io</a>
              </li>
            </ul>
          </div>

          {/* Navigation */}
          <div>
            <h4 className="font-bold text-lg mb-6">Navigation</h4>
            <ul className="space-y-3 text-sm text-gray-400">
              <li><Link href="#parcours" className="hover:text-teal-400 transition-colors">Parcours Fondateur</Link></li>
              <li><Link href="#solutions" className="hover:text-teal-400 transition-colors">Solutions Corporate</Link></li>
              <li><Link href="#investisseurs" className="hover:text-teal-400 transition-colors">Investisseurs</Link></li>
              <li><Link href="#products" className="hover:text-teal-400 transition-colors">Nos Produits</Link></li>
            </ul>
          </div>

          {/* Mentions Légales */}
          <div>
            <h4 className="font-bold text-lg mb-6">Mentions Légales</h4>
            <ul className="space-y-3 text-sm text-gray-400">
              <li><span className="font-bold text-white">RC :</span> 165795</li>
              <li><span className="font-bold text-white">ICE :</span> 003684652000068</li>
            </ul>
            <div className="mt-8">
               <span className="bg-[#002B49] px-4 py-2 rounded text-xs text-teal-400 border border-teal-500/30">© Site Corporate</span>
            </div>
          </div>
        </div>

        <div className="pt-8 flex flex-col md:flex-row justify-between items-center text-xs text-gray-500">
          <p>© 2024 Shabaka InnovLab. Tous droits réservés.</p>
          <div className="flex gap-6 mt-4 md:mt-0">
            <Link href="#" className="hover:text-white transition-colors">Politique de Confidentialité</Link>
            <Link href="#" className="hover:text-white transition-colors">Conditions Générales</Link>
          </div>
        </div>
      </div>
    </footer>
  );
}
