export default function AboutPage() {
  return (
    <div className="mx-auto max-w-4xl px-6 py-12 text-slate-50">
      <h1 className="text-3xl font-semibold tracking-tight">About the Hub</h1>
      <p className="mt-3 text-sm text-slate-300">
        This project is built for the problem statement{" "}
        <span className="font-semibold text-emerald-300">
          “AI for Communities, Access &amp; Public Impact”
        </span>
        . The goal is to explore how AI can meaningfully expand access to
        information, resources, and opportunities for people who are often left
        out of digital systems.
      </p>

      <div className="mt-8 grid gap-6 md:grid-cols-2">
        <div className="rounded-2xl border border-slate-800 bg-slate-950/60 p-5">
          <h2 className="text-sm font-semibold text-slate-100">
            What this hub could power
          </h2>
          <ul className="mt-3 space-y-2 text-xs text-slate-300">
            <li>• Civic information and public service assistants</li>
            <li>• Awareness and skill-development journeys for youth</li>
            <li>
              • AI tools that help communities access schemes, markets, or
              livelihood programs
            </li>
            <li>• Local-language, voice-first, and low-bandwidth flows</li>
          </ul>
        </div>
        <div className="rounded-2xl border border-slate-800 bg-slate-950/60 p-5">
          <h2 className="text-sm font-semibold text-slate-100">
            Design principles
          </h2>
          <ul className="mt-3 space-y-2 text-xs text-slate-300">
            <li>• Start with real community needs, not just features.</li>
            <li>• Prioritise inclusion, safety, and explainability.</li>
            <li>• Optimise for low data, low friction, and assisted use.</li>
            <li>• Make it easy for NGOs and public systems to plug in.</li>
          </ul>
        </div>
      </div>

      <div className="mt-10 rounded-2xl border border-emerald-400/40 bg-emerald-950/40 p-6 text-xs text-emerald-50">
        <h2 className="text-sm font-semibold text-emerald-200">
          Behind the scenes (tech)
        </h2>
        <p className="mt-2">
          The frontend is a Next.js app, while a Python FastAPI backend
          exposes authentication and blog APIs. This separation keeps the UI
          flexible while allowing you to plug in different AI models, retrieval
          systems, or data sources on the backend.
        </p>
      </div>
    </div>
  );
}

