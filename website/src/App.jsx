import { useMemo, useState } from "react";

const platforms = ["All", "LeetCode", "Deep-ML"];

const sampleProblems = [
  { id: 1, title: "Two Sum", platform: "LeetCode", difficulty: "Easy", topic: "Arrays & Hashing", status: "Solved" },
  { id: 206, title: "Reverse Linked List", platform: "LeetCode", difficulty: "Easy", topic: "Linked List", status: "Solved" },
  { id: "ml-01", title: "Sample Deep-ML Problem", platform: "Deep-ML", difficulty: "Medium", topic: "Machine Learning", status: "Solved" }
];

export default function App() {
  const [platform, setPlatform] = useState("All");
  const [query, setQuery] = useState("");

  const problems = useMemo(() => sampleProblems.filter((p) =>
    (platform === "All" || p.platform === platform) &&
    (p.title.toLowerCase().includes(query.toLowerCase()) ||
      p.topic.toLowerCase().includes(query.toLowerCase()))
  ), [platform, query]);

  return (
    <main className="app">
      <header className="header">
        <div>
          <p className="eyebrow">PERSONAL LEARNING OS</p>
          <h1>Revision Dashboard</h1>
          <p className="muted">One place for LeetCode, Deep-ML and everything you solve.</p>
        </div>
        <button className="primary">Start revision</button>
      </header>

      <section className="stats">
        <Stat label="Problems solved" value="299" />
        <Stat label="Platforms" value="2" />
        <Stat label="Topics" value="94" />
        <Stat label="Revised" value="0%" />
      </section>

      <section className="toolbar">
        <div className="tabs">
          {platforms.map((item) => (
            <button key={item} className={platform === item ? "tab active" : "tab"} onClick={() => setPlatform(item)}>
              {item}
            </button>
          ))}
        </div>
        <input
          value={query}
          onChange={(e) => setQuery(e.target.value)}
          placeholder="Search problems or topics..."
        />
      </section>

      <section>
        <div className="section-heading">
          <h2>Problems</h2>
          <span>{problems.length} shown</span>
        </div>
        <div className="problem-list">
          {problems.map((problem) => (
            <article className="problem" key={problem.id}>
              <div className="problem-id">#{problem.id}</div>
              <div className="problem-main">
                <h3>{problem.title}</h3>
                <div className="meta">
                  <span>{problem.platform}</span>
                  <span>{problem.difficulty}</span>
                  <span>{problem.topic}</span>
                </div>
              </div>
              <span className="status">{problem.status}</span>
            </article>
          ))}
        </div>
      </section>
    </main>
  );
}

function Stat({ label, value }) {
  return (
    <div className="stat">
      <strong>{value}</strong>
      <span>{label}</span>
    </div>
  );
}