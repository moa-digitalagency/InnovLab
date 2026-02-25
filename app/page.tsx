import Header from './components/Header';
import Hero from './components/Hero';
import Journey from './components/Journey';
import B2B from './components/B2B';
import Approach from './components/Approach';
import Sectors from './components/Sectors';
import Pillars from './components/Pillars';
import Testimonials from './components/Testimonials';
import Footer from './components/Footer';

export default function Home() {
  return (
    <main className="min-h-screen bg-white">
      <Header />
      <Hero />
      <Journey />
      <B2B />
      <Approach />
      <Sectors />
      <Pillars />
      <Testimonials />
      <Footer />
    </main>
  );
}
