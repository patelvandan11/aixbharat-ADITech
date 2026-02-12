export default function Home() {
  return (
    <div className="mx-auto flex min-h-[calc(100vh-4rem)] max-w-6xl flex-col gap-10 px-6 py-12 text-slate-50">
      <section className="grid gap-10 md:grid-cols-[3fr,2fr] items-center">
        <div className="space-y-6">
          <p className="inline-flex rounded-full bg-emerald-400/10 px-3 py-1 text-xs font-medium text-emerald-300 ring-1 ring-emerald-400/30">
            AI for Communities, Access &amp; Public Impact
          </p>
          <h1 className="text-3xl md:text-4xl lg:text-5xl font-semibold tracking-tight">
            Build AI that helps{" "}
            <span className="text-emerald-300">real communities</span> access
            information, opportunities, and public services.
          </h1>
          <p className="max-w-xl text-sm md:text-base text-slate-300">
            This hub showcases how AI can power civic assistants, local-language
            tools, and low-bandwidth experiences so more people can find
            schemes, resources, and skilling programs that actually change
            lives.
          </p>
          <div className="flex flex-wrap gap-4">
            <a
              href="/signup"
              className="inline-flex items-center rounded-full bg-emerald-400 px-5 py-2 text-sm font-medium text-slate-950 hover:bg-emerald-300 transition-colors"
            >
              Join the community
            </a>
            <a
              href="/blogs"
              className="inline-flex items-center rounded-full border border-slate-700 px-5 py-2 text-sm font-medium text-slate-50 hover:border-emerald-400 hover:text-emerald-200 transition-colors"
            >
              Explore impact stories
            </a>
          </div>
          <div className="grid gap-4 text-xs text-slate-300 sm:grid-cols-3">
            <div className="rounded-xl border border-slate-800 bg-slate-900/40 p-4">
              <p className="font-semibold text-slate-100">
                Civic info assistants
              </p>
              <p className="mt-1">
                Help people ask natural questions about schemes, benefits, and
                services in their own language.
              </p>
            </div>
            <div className="rounded-xl border border-slate-800 bg-slate-900/40 p-4">
              <p className="font-semibold text-slate-100">
                Access &amp; inclusion
              </p>
              <p className="mt-1">
                Design for low-bandwidth, voice-first, and assisted access
                contexts from day one.
              </p>
            </div>
            <div className="rounded-xl border border-slate-800 bg-slate-900/40 p-4">
              <p className="font-semibold text-slate-100">
                Skills &amp; awareness
              </p>
              <p className="mt-1">
                Offer bite-sized, contextual learning journeys to build digital
                and livelihood skills.
              </p>
            </div>
          </div>
        </div>
        <div className="space-y-4 rounded-2xl border border-emerald-400/40 bg-gradient-to-b from-slate-900 to-slate-950 p-6 shadow-[0_0_80px_rgba(16,185,129,0.25)]">
          <p className="text-xs font-medium uppercase tracking-[0.2em] text-emerald-200">
            Community signals
          </p>
          <div className="space-y-3 text-xs text-slate-200">
            <div className="flex items-start justify-between gap-4 rounded-xl bg-slate-900/80 p-3">
              <div>
                <p className="font-semibold">
                  Rural learners accessing skill videos
                </p>
                <p className="text-slate-400">
                  AI curates offline-first pathways in local language.
                </p>
              </div>
              <span className="text-emerald-300 font-semibold">+68%</span>
            </div>
            <div className="flex items-start justify-between gap-4 rounded-xl bg-slate-900/80 p-3">
              <div>
                <p className="font-semibold">
                  Citizens discovering welfare schemes
                </p>
                <p className="text-slate-400">
                  Guided conversations reduce drop-offs in applications.
                </p>
              </div>
              <span className="text-emerald-300 font-semibold">3x</span>
            </div>
            <div className="flex items-start justify-between gap-4 rounded-xl bg-slate-900/80 p-3">
              <div>
                <p className="font-semibold">
                  NGOs mapping local opportunities
                </p>
                <p className="text-slate-400">
                  AI surfaces relevant programs, markets, and partners.
                </p>
              </div>
              <span className="text-emerald-300 font-semibold">+42%</span>
            </div>
          </div>
          <p className="text-[11px] text-slate-500">
            These are illustrative signals for the hackathon problem statement:
            how AI can expand access to information, resources, and opportunity.
          </p>
        </div>
      </section>
    </div>
  );
}
