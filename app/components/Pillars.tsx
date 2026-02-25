'use client';

import { motion } from 'framer-motion';
import { Code, BrainCircuit, Rocket, Scale, Banknote } from 'lucide-react';

const pillars = [
  {
    icon: Code,
    title: "Studio Dev",
    desc: "Développement agile, architecture scalable et MVP factory.",
    color: "bg-blue-50 text-blue-600"
  },
  {
    icon: BrainCircuit,
    title: "Expertise IA/Cyber",
    desc: "Intégration d'IA de pointe et bouclier de cybersécurité.",
    color: "bg-teal-50 text-teal-600"
  },
  {
    icon: Rocket,
    title: "Accélération",
    desc: "Programme intensif de croissance et Go-to-Market.",
    color: "bg-orange-50 text-orange-600"
  },
  {
    icon: Scale,
    title: "Légal",
    desc: "Ingénierie juridique, conformité et propriété intellectuelle.",
    color: "bg-purple-50 text-purple-600"
  },
  {
    icon: Banknote,
    title: "Finance",
    desc: "Structuration financière, levée de fonds et gestion trésorerie.",
    color: "bg-green-50 text-green-600"
  }
];

export default function Pillars() {
  return (
    <section className="py-24 bg-gray-50" id="expertise">
      <div className="container mx-auto px-6">
        <div className="text-center mb-16">
          <span className="text-[#006D77] font-semibold tracking-wider text-sm uppercase">Notre Architecture</span>
          <h2 className="text-3xl md:text-4xl font-bold text-[#002B49] mt-2 mb-4">Les 5 Piliers de l&apos;Excellence</h2>
        </div>

        <div className="grid grid-cols-1 sm:grid-cols-2 lg:grid-cols-5 gap-6">
          {pillars.map((pillar, index) => (
            <motion.div
              key={index}
              className="bg-white p-6 rounded-xl shadow-sm hover:shadow-md transition-shadow text-center group"
              whileHover={{ y: -5 }}
              initial={{ opacity: 0, y: 20 }}
              whileInView={{ opacity: 1, y: 0 }}
              viewport={{ once: true }}
              transition={{ delay: index * 0.1 }}
            >
              <div className={`w-14 h-14 ${pillar.color} rounded-full flex items-center justify-center mx-auto mb-4 group-hover:scale-110 transition-transform`}>
                <pillar.icon className="w-7 h-7" />
              </div>
              <h3 className="text-lg font-bold text-[#002B49] mb-2">{pillar.title}</h3>
              <p className="text-xs text-gray-500 leading-relaxed">{pillar.desc}</p>
            </motion.div>
          ))}
        </div>
      </div>
    </section>
  );
}
