import { useMemo, useState } from "react";

const platforms = ["All", "LeetCode", "Deep-ML"];
const sampleProblems = [
  { id: 1, title: "Two Sum", platform: "LeetCode", difficulty: "Easy", topic: "Arrays & Hashing", status: "Solved" },
  { id: 206, title: "Reverse Linked List", platform: "LeetCode", difficulty: "Easy", topic: "Linked List", status: "Solved" },
  { id: "ml-01", title: "Sample Deep-ML Problem", platform: "Deep-ML", difficulty: "Medium", topic: "Machine Learning", status: "Solved" }
];

const roadmaps = [
  { title: "Build a RAG Application", description: "From embeddings and retrieval to a production-ready RAG pipeline.", progress: 35, steps: ["Learn embeddings", "Build a vector store", "Implement retrieval", "Add generation", "Evaluate the pipeline"] },
  { title: "Master Transformers", description: "A focused path through attention, positional encoding and modern LLM architecture.", progress: 20, steps: ["Attention & QKV", "Positional encoding", "Transformer blocks", "Training objectives", "Build a mini transformer"] },
  { title: "Interview DSA Revision", description: "Revisit the patterns behind your solved problems and close weak areas.", progress: 42, steps: ["Arrays & hashing", "Two pointers", "Trees & graphs", "Dynamic programming", "Mixed revision"] }
];

export default function App() {
  const [platform, setPlatform] = useState("All");
  const [query, setQuery] = useState("");
  const [view, setView] = useState("overview");
  const problems = useMemo(() => sampleProblems.filter((p) =>
    (platform === "All" || p.platform === platform) &&
    (p.title.toLowerCase().includes(query.toLowerCase()) || p.topic.toLowerCase().includes(query.toLowerCase()))
  ), [platform, query]);

  return (
    <main className="app">
      <nav className="nav">
        <button className="brand" onClick={() => setView("overview")}>LEARNING OS</button>
        <div className="nav-links">
          <button className={view === "overview" ? "nav-link active" : "nav-link"} onClick={() => setView("overview")}>Overview</button>
          <button className={view === "roadmaps" ? "nav-link active" : "nav-link"} onClick={() => setView("roadmaps")}>Roadmaps</button>
          <button className={view === "problems" ? "nav-link active" : "nav-link"} onClick={() => setView("problems")}>Problems</button>
        </div>
      </nav>

      {view === "roadmaps" ? <Roadmaps /> : (
        <>
          <header className="header">
            <div>
              <p className="eyebrow">PERSONAL LEARNING OS</p>
              <h1>Build. Learn. Revise.</h1>
              <p className="muted">One minimal workspace for everything you're learning.</p>
            </div>
            <button className="primary" onClick={() => setView("roadmaps")}>View roadmaps</button>
          </header>

          <section className="stats">
            <Stat label="Problems solved" value="299" />
            <Stat label="Platforms" value="2" />
            <Stat label="Topics" value="94" />
            <Stat label="Revised" value="0%" />
          </section>

          <section className="focus">
            <div>
              <p className="eyebrow">CURRENT FOCUS</p>
              <h2>Build your next project</h2>
              <p className="muted">Choose a roadmap and work through it step by step.</p>
            </div>
            <button className="text-button" onClick={() => setView("roadmaps")}>Explore roadmaps →</button>
          </section>

          <section>
            <div className="section-heading"><h2>Problems</h2><span>{problems.length} shown</span></div>
            <section className="toolbar">
              <div className="tabs">{platforms.map((item) => (
                <button key={item} className={platform === item ? "tab active" : "tab"} onClick={() => setPlatform(item)}>{item}</button>
              ))}</div>
              <input value={query} onChange={(e) => setQuery(e.target.value)} placeholder="Search problems or topics..." />
            </section>
            <div className="problem-list">
              {problems.map((problem) => <article className="problem" key={problem.id}>
                <div className="problem-id">#{problem.id}</div>
                <div><h3>{problem.title}</h3><div className="meta"><span>{problem.platform}</span><span>{problem.difficulty}</span><span>{problem.topic}</span></div></div>
                <span className="status">{problem.status}</span>
              </article>)}
            </div>
          </section>
        </>
      )}
    </main>
  );
}

function Roadmaps() {
  return (
    <>
      <header className="page-header">
        <p className="eyebrow">LEARNING PATHS</p>
        <h1>Roadmaps</h1>
        <p className="muted">Turn a goal into a sequence of small, actionable steps.</p>
      </header>
      <section className="roadmap-grid">
        {roadmaps.map((roadmap) => (
          <article className="roadmap" key={roadmap.title}>
            <div className="roadmap-top"><span className="roadmap-label">ROADMAP</span><span>{roadmap.progress}%</span></div>
            <h2>{roadmap.title}</h2>
            <p>{roadmap.description}</p>
            <div className="progress"><span style={{ width: `${roadmap.progress}%` }} /></div>
            <ol>{roadmap.steps.map((step, i) => <li key={step} className={i < Math.floor(roadmap.steps.length * roadmap.progress / 100) ? "done" : ""}>{step}</li>)}</ol>
            <button className="roadmap-action">Continue →</button>
          </article>
        ))}
      </section>
      <section className="agent-box">
        <div><p className="eyebrow">AI ROADMAP BUILDER</p><h2>Don't know what to learn next?</h2><p className="muted">Later, connect an AI agent here to turn a goal like “build a production RAG app” into a personalized roadmap.</p></div>
        <button className="primary">Create roadmap</button>
      </section>
    </>
  );
}

function Stat({ label, value }) { return <div className="stat"><strong>{value}</strong><span>{label}</span></div>; }