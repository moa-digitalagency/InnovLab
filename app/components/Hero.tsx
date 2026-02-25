'use client';

import { motion } from 'framer-motion';
import { Rocket, Building, TrendingUp } from 'lucide-react';

export default function Hero() {
  const containerVariants = {
    hidden: { opacity: 0 },
    visible: {
      opacity: 1,
      transition: {
        staggerChildren: 0.2,
      },
    },
  };

  const itemVariants = {
    hidden: { opacity: 0, y: 20 },
    visible: {
      opacity: 1,
      y: 0,
      transition: {
        duration: 0.6,
        ease: "easeOut" as const,
      },
    },
  };

  return (
    <section className="relative pt-20 pb-32 overflow-hidden bg-gradient-to-b from-[#f0f9ff] to-white">
      {/* Background decoration */}
      <div className="absolute top-0 left-0 w-full h-full overflow-hidden z-0">
        <div className="absolute top-[-20%] right-[-10%] w-[600px] h-[600px] bg-blue-100 rounded-full blur-[100px] opacity-40"></div>
        <div className="absolute bottom-[-20%] left-[-10%] w-[500px] h-[500px] bg-teal-100 rounded-full blur-[100px] opacity-40"></div>
      </div>

      <div className="container mx-auto px-6 relative z-10">
        <motion.div
          className="text-center max-w-4xl mx-auto mb-16"
          variants={containerVariants}
          initial="hidden"
          animate="visible"
        >
          <motion.div variants={itemVariants} className="inline-block px-4 py-1.5 bg-teal-50 text-[#006D77] rounded-full text-sm font-semibold mb-6 border border-teal-100">
            ★ ECOSYSTEME D&apos;EXCELLENCE PANAFRICAIN ★
          </motion.div>

          <motion.h1 variants={itemVariants} className="text-4xl md:text-6xl font-extrabold text-[#002B49] leading-tight mb-6">
            Le Catalyseur de la <br className="hidden md:block" />
            <span className="text-[#006D77]">Souveraineté Technologique</span> <br className="hidden md:block" />
            Africaine
          </motion.h1>

          <motion.p variants={itemVariants} className="text-lg md:text-xl text-gray-600 max-w-2xl mx-auto leading-relaxed">
            Une plateforme unique fusionnant innovation de rupture, puissance corporative et capital intelligent pour bâtir les géants de demain.
          </motion.p>
        </motion.div>

        <motion.div
          className="grid md:grid-cols-3 gap-6 max-w-5xl mx-auto"
          variants={containerVariants}
          initial="hidden"
          whileInView="visible"
          viewport={{ once: true }}
        >
          {/* Card 1 */}
          <motion.div variants={itemVariants} className="bg-white p-8 rounded-2xl shadow-xl border border-gray-100 hover:border-teal-200 transition-all duration-300 transform hover:-translate-y-1 group cursor-pointer text-center">
            <div className="w-16 h-16 bg-blue-50 rounded-full flex items-center justify-center mx-auto mb-6 group-hover:bg-[#002B49] transition-colors duration-300">
              <Rocket className="w-8 h-8 text-[#002B49] group-hover:text-white transition-colors duration-300" />
            </div>
            <h3 className="text-xl font-bold text-[#002B49] mb-2">Je suis Fondateur</h3>
            <p className="text-gray-500">Accélérez votre vision</p>
          </motion.div>

          {/* Card 2 */}
          <motion.div variants={itemVariants} className="bg-white p-8 rounded-2xl shadow-xl border border-gray-100 hover:border-teal-200 transition-all duration-300 transform hover:-translate-y-1 group cursor-pointer text-center">
            <div className="w-16 h-16 bg-teal-50 rounded-full flex items-center justify-center mx-auto mb-6 group-hover:bg-[#006D77] transition-colors duration-300">
              <Building className="w-8 h-8 text-[#006D77] group-hover:text-white transition-colors duration-300" />
            </div>
            <h3 className="text-xl font-bold text-[#002B49] mb-2">Je suis Corporate</h3>
            <p className="text-gray-500">Co-construisez le futur</p>
          </motion.div>

          {/* Card 3 */}
          <motion.div variants={itemVariants} className="bg-white p-8 rounded-2xl shadow-xl border border-gray-100 hover:border-teal-200 transition-all duration-300 transform hover:-translate-y-1 group cursor-pointer text-center">
            <div className="w-16 h-16 bg-green-50 rounded-full flex items-center justify-center mx-auto mb-6 group-hover:bg-[#8BC53F] transition-colors duration-300">
              <TrendingUp className="w-8 h-8 text-[#8BC53F] group-hover:text-white transition-colors duration-300" />
            </div>
            <h3 className="text-xl font-bold text-[#002B49] mb-2">Je suis Investisseur</h3>
            <p className="text-gray-500">Financez l&apos;impact</p>
          </motion.div>
        </motion.div>
      </div>
    </section>
  );
}
