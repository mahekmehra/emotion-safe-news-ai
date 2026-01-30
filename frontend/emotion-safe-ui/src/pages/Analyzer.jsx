import { useState } from "react";
import { analyzeText } from "../api/analyze";
import TextInput from "../components/TextInput";
import RiskBadge from "../components/RiskBadge";
import EmotionHighlights from "../components/EmotionHighlights";
import RewriteBox from "../components/RewriteBox";

export default function Analyzer() {
  const [data, setData] = useState(null);
  const [loading, setLoading] = useState(false);
  const [originalText, setOriginalText] = useState("");

  async function handleAnalyze(payload) {
    setLoading(true);
    setOriginalText(payload.text); // ✅ store text safely

    try {
      const response = await analyzeText(payload);
      setData(response);
    } finally {
      setLoading(false);
    }
  }

  return (
    <div className="container">
      <TextInput onAnalyze={handleAnalyze} />

      {loading && (
        <p style={{ marginTop: "1rem" }}>
          🧠 Analyzing content responsibly…
        </p>
      )}

      {data && (
        <>
          <RiskBadge badge={data.risk_badge} />

          <EmotionHighlights
            text={originalText}
            highlights={data.highlights}
          />

          <h3>Explanation</h3>
          <p>{data.explanation}</p>

          <RewriteBox rewritten={data.rewritten_text} />
        </>
      )}
    </div>
  );
}
