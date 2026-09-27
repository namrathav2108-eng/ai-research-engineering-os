"use client";

export default function Home() {
  return (
    <main className="min-h-screen bg-slate-950 text-white">
      <div className="mx-auto max-w-7xl px-6 py-10">
        <header className="mb-10">
          <p className="mb-2 text-sm font-medium text-blue-400">
            AI RESEARCH & ENGINEERING OS
          </p>

          <h1 className="text-4xl font-bold tracking-tight">
            Your intelligent research workspace.
          </h1>

          <p className="mt-3 max-w-2xl text-slate-400">
            Research papers, experiments, code, datasets and AI agents —
            organized in one intelligent workspace.
          </p>
        </header>

        <section className="grid gap-5 md:grid-cols-2 lg:grid-cols-3">
          <div className="rounded-2xl border border-slate-800 bg-slate-900 p-6">
            <div className="mb-4 text-2xl">Research Library</div>
            <h2 className="text-xl font-semibold">Research Library</h2>
            <p className="mt-2 text-sm text-slate-400">
              Upload and organize research papers, documents and datasets.
            </p>
          </div>

          <div className="rounded-2xl border border-slate-800 bg-slate-900 p-6">
            <div className="mb-4 text-2xl">AI Assistant</div>
            <h2 className="text-xl font-semibold">AI Research Assistant</h2>
            <p className="mt-2 text-sm text-slate-400">
              Ask questions, compare papers and discover research insights.
            </p>
          </div>

          <div className="rounded-2xl border border-slate-800 bg-slate-900 p-6">
            <div className="mb-4 text-2xl">Experiments</div>
            <h2 className="text-xl font-semibold">Experiments</h2>
            <p className="mt-2 text-sm text-slate-400">
              Track models, datasets, metrics and experiment results.
            </p>
          </div>

          <div className="rounded-2xl border border-slate-800 bg-slate-900 p-6">
            <div className="mb-4 text-2xl">Search</div>
            <h2 className="text-xl font-semibold">Intelligent Search</h2>
            <p className="mt-2 text-sm text-slate-400">
              Search your entire research knowledge base using AI.
            </p>
          </div>

          <div className="rounded-2xl border border-slate-800 bg-slate-900 p-6">
            <div className="mb-4 text-2xl">Code</div>
            <h2 className="text-xl font-semibold">Code Intelligence</h2>
            <p className="mt-2 text-sm text-slate-400">
              Understand repositories, experiments and engineering workflows.
            </p>
          </div>

          <div className="rounded-2xl border border-slate-800 bg-slate-900 p-6">
            <div className="mb-4 text-2xl">Analytics</div>
            <h2 className="text-xl font-semibold">Analytics</h2>
            <p className="mt-2 text-sm text-slate-400">
              Monitor research progress, experiments and evaluation metrics.
            </p>
          </div>
        </section>
      </div>
    </main>
  );
}
