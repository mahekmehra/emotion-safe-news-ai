import { useState } from "react";

export default function TextInput({ onAnalyze }) {
  const [text, setText] = useState("");
  const [tone, setTone] = useState("neutral");

  return (
    <div>
      <h3>Enter Content</h3>

      <textarea
        rows="6"
        style={{ width: "100%" }}
        placeholder="Paste news text here..."
        value={text}
        onChange={(e) => setText(e.target.value)}
      />

      <div style={{ marginTop: "1rem" }}>
        <label>Rewrite Tone: </label>
        <select value={tone} onChange={(e) => setTone(e.target.value)}>
          <option value="neutral">Neutral</option>
          <option value="educational">Educational</option>
          <option value="reassuring">Reassuring</option>
        </select>
      </div>

      <button
        style={{ marginTop: "1rem" }}
        onClick={() => onAnalyze({ text, tone })}
        disabled={!text.trim()}
      >
        Analyze
      </button>
    </div>
  );
}
