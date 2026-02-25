'use client';

import { motion } from 'framer-motion';
import { Quote } from 'lucide-react';

export default function Testimonials() {
  const testimonials = [
    {
      role: "FOUNDER",
      content: "L'infrastructure de Shabaka nous a permis de passer de l'idée au produit en 4 mois. C'est l'accélérateur ultime pour tout fondateur tech en Afrique.",
      author: "Dr. Kalenji",
      title: "Founder, Med-Orkidi AI",
      dark: false
    },
    {
      role: "CORPORATE",
      content: "Une collaboration fluide. Shabaka nous a connectés aux technologies de rupture dont nous avions besoin pour moderniser nos processus internes.",
      author: "Directeur CTO",
      title: "Grand Groupe Industriel",
      dark: true
    },
    {
      role: "STARTUP CEO",
      content: "La plus précieuse ? La communauté. Être entouré de fondateurs qui font face aux mêmes défis change tout. On grandit ensemble.",
      author: "Sarah L.",
      title: "CEO, Agri-Solutions",
      dark: false
    }
  ];

  return (
    <section className="py-24 bg-white" id="testimonials">
      <div className="container mx-auto px-6">
        <div className="text-center mb-16">
          <h2 className="text-3xl md:text-4xl font-bold text-[#002B49] mb-4">Échos de l&apos;Écosystème</h2>
          <p className="text-gray-500">Ils bâtissent l&apos;Afrique de demain avec Shabaka InnovLab.</p>
        </div>

        <div className="grid grid-cols-1 md:grid-cols-3 gap-8">
          {testimonials.map((t, index) => (
            <motion.div
              key={index}
              className={`p-8 rounded-2xl relative ${t.dark ? 'bg-[#002B49] text-white shadow-xl transform md:-translate-y-4' : 'bg-gray-50 text-gray-700'}`}
              initial={{ opacity: 0, y: 20 }}
              whileInView={{ opacity: 1, y: 0 }}
              viewport={{ once: true }}
              transition={{ delay: index * 0.2 }}
            >
              <Quote className={`w-8 h-8 mb-6 ${t.dark ? 'text-teal-500' : 'text-gray-300'}`} />

              <div className={`text-xs font-bold tracking-wider mb-4 px-2 py-1 inline-block rounded ${t.dark ? 'bg-white/10 text-teal-400' : 'bg-green-100 text-green-700'}`}>
                {t.role}
              </div>

              <p className={`text-sm leading-relaxed mb-6 italic ${t.dark ? 'text-gray-300' : 'text-gray-600'}`}>
                &quot;{t.content}&quot;
              </p>

              <div className="flex items-center gap-3">
                <div className={`w-10 h-10 rounded-full flex items-center justify-center font-bold text-sm ${t.dark ? 'bg-teal-500 text-white' : 'bg-[#002B49] text-white'}`}>
                  {t.author.charAt(0)}
                </div>
                <div>
                  <div className={`font-bold text-sm ${t.dark ? 'text-white' : 'text-[#002B49]'}`}>{t.author}</div>
                  <div className={`text-xs ${t.dark ? 'text-gray-400' : 'text-gray-500'}`}>{t.title}</div>
                </div>
              </div>
            </motion.div>
          ))}
        </div>
      </div>
    </section>
  );
}
