'use client';

import { motion } from 'framer-motion';
import { Home, Scale, Ambulance, Cpu } from 'lucide-react';

export default function Sectors() {
  return (
    <section className="py-24 bg-white" id="sectors">
      <div className="container mx-auto px-6">
        <div className="text-center mb-16">
          <span className="text-[#006D77] font-semibold tracking-wider text-sm uppercase">Nos fers de lance</span>
          <h2 className="text-3xl md:text-4xl font-bold text-[#002B49] mt-2 mb-4">Forteresses Sectorielles</h2>
        </div>

        <div className="grid grid-cols-1 md:grid-cols-2 gap-8">
          {/* Main Large Card (Shabaka Syndic) */}
          <motion.div
            className="md:col-span-1 bg-gray-50 rounded-3xl p-8 hover:shadow-xl transition-shadow relative overflow-hidden group"
            whileHover={{ y: -5 }}
          >
            <div className="flex items-center gap-3 mb-4">
              <div className="bg-white p-2 rounded-lg shadow-sm">
                 <Home className="w-5 h-5 text-gray-700" />
              </div>
              <span className="text-xs font-bold text-gray-400 tracking-wider">PROPTECH</span>
            </div>

            <h3 className="text-2xl font-bold text-[#002B49] mb-3">Shabaka Syndic</h3>
            <p className="text-gray-500 mb-8 max-w-sm">
              La plateforme de référence pour la gestion de copropriété digitale, automatisant 90% des tâches administratives.
            </p>

            <div className="w-full h-48 bg-[#2C3E50] rounded-xl shadow-inner mt-4 transform translate-y-4 group-hover:translate-y-2 transition-transform duration-500 flex items-end justify-center pb-4 opacity-90">
               {/* UI Mockup Placeholder */}
               <div className="w-3/4 h-3/4 bg-gray-700 rounded-t-lg border-t-2 border-l-2 border-r-2 border-gray-600"></div>
            </div>

            <div className="absolute bottom-8 left-8">
               <div className="text-3xl font-bold text-[#006D77]">+150%</div>
               <div className="text-xs text-gray-400 uppercase tracking-wide">Croissance Utilisateurs / An</div>
            </div>
          </motion.div>

          <div className="md:col-span-1 grid grid-cols-1 gap-8">
             {/* LexIA (Dark Card) */}
             <motion.div
                className="bg-[#002B49] rounded-3xl p-8 text-white relative overflow-hidden"
                whileHover={{ y: -5 }}
             >
                <div className="relative z-10">
                   <div className="flex items-center gap-3 mb-4">
                      <div className="bg-white/10 p-2 rounded-lg backdrop-blur-sm">
                         <Scale className="w-5 h-5 text-white" />
                      </div>
                      <span className="text-xs font-bold text-gray-400 tracking-wider">LEGALTECH</span>
                   </div>
                   <h3 className="text-2xl font-bold mb-2">LexIA</h3>
                   <p className="text-gray-300 text-sm mb-4">L&apos;intelligence artificielle au service de la démocratisation juridique.</p>
                   <div className="text-right text-4xl font-black text-white/5 uppercase tracking-widest absolute bottom-4 right-4 pointer-events-none">LEGAL</div>
                </div>
             </motion.div>

             {/* Bottom 2 Small Cards */}
             <div className="grid grid-cols-2 gap-8">
                {/* Urgence Gabon */}
                <motion.div
                   className="bg-teal-50 rounded-3xl p-6 hover:shadow-lg transition-shadow"
                   whileHover={{ y: -5 }}
                >
                   <Ambulance className="w-6 h-6 text-teal-600 mb-4" />
                   <h3 className="font-bold text-[#002B49] mb-2">Urgence Gabon</h3>
                   <p className="text-xs text-gray-500 mb-4">Optimisation logistique des secours.</p>
                   <span className="text-teal-600 text-xs font-bold">24/7 Ops</span>
                </motion.div>

                {/* AI Manager */}
                <motion.div
                   className="bg-white border border-gray-100 rounded-3xl p-6 hover:shadow-lg transition-shadow"
                   whileHover={{ y: -5 }}
                >
                   <Cpu className="w-6 h-6 text-purple-600 mb-4" />
                   <h3 className="font-bold text-[#002B49] mb-2">AI Manager</h3>
                   <p className="text-xs text-gray-500 mb-4">Le futur des ressources humaines.</p>
                   <div className="w-full h-1 bg-gray-100 rounded-full overflow-hidden">
                      <div className="h-full w-2/3 bg-purple-500 rounded-full"></div>
                   </div>
                </motion.div>
             </div>
          </div>
        </div>
      </div>
    </section>
  );
}
