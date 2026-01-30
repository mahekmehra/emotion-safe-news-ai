export default function RewriteBox({ rewritten }) {
  if (!rewritten) return null;

  return (
    <div>
      <h3>Rewritten Content (Mental-Health Safe)</h3>
      <div
        style={{
          background: "#f1f5f9",
          padding: "1rem",
          borderRadius: "8px",
          whiteSpace: "pre-wrap",
          lineHeight: "1.6",
        }}
      >
        {rewritten}
      </div>
    </div>
  );
}
