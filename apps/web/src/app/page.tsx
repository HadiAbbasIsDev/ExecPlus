/* Use case: Provides the initial product-facing web route.
What it does: Communicates the verified analytics workflow and current engineering phase without implying unfinished features exist. */

const foundations = [
  "Workspace-first isolation",
  "Database-executed numbers",
  "Calculation lineage",
  "Replaceable AI providers",
];

const upcoming = [
  "Secure CSV and XLSX ingestion",
  "Deterministic dataset profiles",
  "Verified conversational queries",
];

export default function Home() {
  return (
    <main>
      <nav aria-label="Primary navigation">
        <a className="brand" href="#top" aria-label="ExecPlus home">
          <span className="brandMark" aria-hidden="true">E+</span>
          <span>ExecPlus</span>
        </a>
        <span className="phaseBadge">Foundation · Phase 0</span>
      </nav>

      <section className="hero" id="top">
        <div className="eyebrow">Operational clarity, backed by evidence</div>
        <h1>Ask your business data.<br />Trust the answer.</h1>
        <p className="heroCopy">
          ExecPlus is being built to turn structured datasets into clear answers,
          explainable charts, and decisions you can verify.
        </p>
        <div className="heroActions">
          <a className="primaryAction" href="#architecture">Explore the foundation</a>
          <span>Alpha workflow under active development</span>
        </div>
      </section>

      <section className="principles" aria-label="Product principles">
        {foundations.map((foundation, index) => (
          <article key={foundation}>
            <span>0{index + 1}</span>
            <h2>{foundation}</h2>
          </article>
        ))}
      </section>

      <section className="architecture" id="architecture">
        <div>
          <div className="eyebrow">Built for measured scale</div>
          <h2>A clean boundary between language and truth.</h2>
          <p>
            Models interpret intent and explain results. A controlled query engine
            computes every number. Each response carries the dataset, operation,
            filters, and record count needed to trace it.
          </p>
        </div>
        <div className="flow" aria-label="ExecPlus request flow">
          <div><span>01</span><strong>Question</strong><small>Plain language</small></div>
          <div><span>02</span><strong>Validate</strong><small>Intent and access</small></div>
          <div><span>03</span><strong>Compute</strong><small>Read-only engine</small></div>
          <div><span>04</span><strong>Explain</strong><small>Answer and lineage</small></div>
        </div>
      </section>

      <section className="next">
        <div>
          <div className="eyebrow">Next delivery phase</div>
          <h2>Secure ingestion and profiling</h2>
        </div>
        <ol>
          {upcoming.map((item) => <li key={item}>{item}</li>)}
        </ol>
      </section>

      <footer>
        <span>ExecPlus</span>
        <span>Exact computation · Explainable results</span>
      </footer>
    </main>
  );
}

