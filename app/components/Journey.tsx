'use client';

import { motion } from 'framer-motion';
import { MapPin, ShieldCheck, Rocket, BarChart2, RefreshCw } from 'lucide-react';

const steps = [
  {
    icon: MapPin,
    title: "L'Étincelle",
    desc: "Idéation & Prototypage",
    sub: "Validé par notre Studio Dev"
  },
  {
    icon: ShieldCheck,
    title: "L'Armure",
    desc: "Structuration Legal &",
    sub: "Sécurisation Cyber"
  },
  {
    icon: Rocket,
    title: "Le Décollage",
    desc: "Go-to-Market agressif &",
    sub: "Premiers clients"
  },
  {
    icon: BarChart2,
    title: "La Traction",
    desc: "Croissance métrique &",
    sub: "Optimisation"
  },
  {
    icon: RefreshCw,
    title: "L'Expansion",
    desc: "Levée de fonds via Shabaka",
    sub: "Invest & Scale-up"
  }
];

export default function Journey() {
  return (
    <section className="py-24 bg-white" id="parcours">
      <div className="container mx-auto px-6">
        <div className="text-center mb-16">
          <span className="text-[#006D77] font-semibold tracking-wider text-sm uppercase">Pour les visionnaires</span>
          <h2 className="text-3xl md:text-4xl font-bold text-[#002B49] mt-2 mb-4">Votre Journey Entrepreneuriale</h2>
          <p className="text-gray-500 max-w-2xl mx-auto">De l&apos;étincelle initiale à l&apos;expansion internationale, nous balisons chaque étape.</p>
        </div>

        <div className="relative">
          {/* Connecting Line */}
          <div className="hidden md:block absolute top-12 left-0 w-full h-1 bg-gray-100 -z-0">
             <div className="absolute top-0 left-0 h-full bg-teal-500 w-1/2 opacity-20"></div> {/* decorative partial fill */}
          </div>

          <div className="grid grid-cols-1 md:grid-cols-5 gap-8 relative z-10">
            {steps.map((step, index) => (
              <motion.div
                key={index}
                className="flex flex-col items-center text-center group"
                initial={{ opacity: 0, y: 20 }}
                whileInView={{ opacity: 1, y: 0 }}
                viewport={{ once: true }}
                transition={{ delay: index * 0.1 }}
              >
                <div className="w-24 h-24 bg-white rounded-full border-4 border-gray-50 flex items-center justify-center mb-6 group-hover:border-teal-500 group-hover:shadow-lg transition-all duration-300">
                  <step.icon className="w-8 h-8 text-[#002B49] group-hover:text-teal-600 transition-colors" />
                </div>

                <div className="bg-teal-700 text-white text-xs font-bold px-3 py-1 rounded-full mb-3">
                  ÉTAPE {index + 1}
                </div>

                <h3 className="text-lg font-bold text-[#002B49] mb-1">{step.title}</h3>
                <p className="text-sm text-gray-500">{step.desc}</p>
                <p className="text-xs text-gray-400 mt-1">{step.sub}</p>
              </motion.div>
            ))}
          </div>
        </div>
      </div>
    </section>
  );
}
