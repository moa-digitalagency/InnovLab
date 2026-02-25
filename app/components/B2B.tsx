'use client';

import { motion } from 'framer-motion';
import { Network, ShieldCheck, Share2 } from 'lucide-react';

export default function B2B() {
  return (
    <section className="py-24 bg-gray-50 overflow-hidden" id="solutions">
      <div className="container mx-auto px-6">
        <div className="flex flex-col md:flex-row items-center gap-16">

          {/* Left Content */}
          <div className="md:w-1/2">
            <span className="text-[#006D77] font-semibold tracking-wider text-sm uppercase block mb-2">Pour les entreprises</span>
            <h2 className="text-4xl md:text-5xl font-extrabold text-[#002B49] mb-6">Co-construisons le Futur</h2>
            <p className="text-lg text-gray-600 mb-8 leading-relaxed">
              Ne subissez pas la disruption, provoquez-la. Nous connectons votre puissance industrielle à l&apos;agilité de nos startups pour créer des avantages concurrentiels durables.
            </p>

            <div className="grid grid-cols-1 sm:grid-cols-2 gap-6">
              <div className="bg-white p-6 rounded-xl shadow-sm hover:shadow-md transition-shadow">
                <Network className="w-10 h-10 text-teal-600 mb-4" />
                <h3 className="font-bold text-[#002B49] text-xl mb-2">Open Innovation</h3>
                <p className="text-sm text-gray-500">Sourcing de startups alignées avec vos enjeux stratégiques.</p>
              </div>

              <div className="bg-white p-6 rounded-xl shadow-sm hover:shadow-md transition-shadow">
                <ShieldCheck className="w-10 h-10 text-blue-600 mb-4" />
                <h3 className="font-bold text-[#002B49] text-xl mb-2">Cyber Shield</h3>
                <p className="text-sm text-gray-500">Audits et protection avancée de vos actifs numériques critiques.</p>
              </div>
            </div>

            <div className="mt-8 flex items-center gap-3">
              <button className="bg-white border border-gray-200 text-[#002B49] px-6 py-2 rounded-full text-sm font-semibold shadow-sm flex items-center gap-2 hover:bg-gray-50 transition-colors">
                <span className="w-2 h-2 rounded-full bg-green-500"></span> Systèmes Opérationnels
              </button>
            </div>
          </div>

          {/* Right Content - Future Proofing Card */}
          <motion.div
            className="md:w-1/2 w-full"
            initial={{ opacity: 0, x: 50 }}
            whileInView={{ opacity: 1, x: 0 }}
            viewport={{ once: true }}
            transition={{ duration: 0.8 }}
          >
            <div className="bg-[#002B49] text-white p-8 md:p-12 rounded-3xl relative shadow-2xl overflow-hidden">
              {/* Decoration */}
              <div className="absolute top-0 right-0 w-64 h-64 bg-teal-500 rounded-full filter blur-[80px] opacity-20 transform translate-x-1/2 -translate-y-1/2"></div>

              <div className="relative z-10">
                <div className="flex justify-between items-start mb-8">
                  <div>
                    <h3 className="text-3xl font-bold mb-1">Future-Proofing</h3>
                    <p className="text-teal-400 text-sm">Indice de résilience technologique</p>
                  </div>
                  <span className="bg-teal-500/20 text-teal-300 px-3 py-1 rounded text-xs font-bold border border-teal-500/30">A+ RATING</span>
                </div>

                {/* Progress Bars */}
                <div className="space-y-6 mb-8">
                  <div>
                    <div className="flex justify-between text-sm mb-2">
                      <span className="text-gray-300">Adoption IA</span>
                      <span className="font-bold">75%</span>
                    </div>
                    <div className="h-2 bg-blue-900 rounded-full overflow-hidden">
                      <motion.div
                        className="h-full bg-gradient-to-r from-teal-400 to-blue-400"
                        initial={{ width: 0 }}
                        whileInView={{ width: "75%" }}
                        transition={{ duration: 1.5, delay: 0.5 }}
                      ></motion.div>
                    </div>
                  </div>

                  <div>
                    <div className="flex justify-between text-sm mb-2">
                      <span className="text-gray-300">Sécurité des Données</span>
                      <span className="font-bold">101%</span>
                    </div>
                    <div className="h-2 bg-blue-900 rounded-full overflow-hidden">
                      <motion.div
                        className="h-full bg-gradient-to-r from-green-400 to-teal-400"
                        initial={{ width: 0 }}
                        whileInView={{ width: "100%" }}
                        transition={{ duration: 1.5, delay: 0.7 }}
                      ></motion.div>
                    </div>
                  </div>
                </div>

                <div className="flex items-start gap-4 p-4 bg-white/5 rounded-xl border border-white/10 backdrop-blur-sm">
                  <div className="bg-teal-500/20 p-2 rounded-lg">
                    <Share2 className="text-teal-400 w-5 h-5" />
                  </div>
                  <p className="text-sm text-gray-300 italic">
                    &quot;L&apos;alliance stratégique entre Corporates et Startups est la clé de la souveraineté.&quot;
                  </p>
                </div>
              </div>
            </div>
          </motion.div>
        </div>
      </div>
    </section>
  );
}
