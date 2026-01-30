export default function RiskBadge({ badge }) {
  if (!badge) return null;

  const colors = {
    green: "#2ecc71",
    yellow: "#f1c40f",
    red: "#e74c3c",
  };

  return (
    <div
      style={{
        background: colors[badge.color],
        color: "#fff",
        padding: "0.5rem 1rem",
        borderRadius: "8px",
        display: "inline-block",
        marginTop: "1rem",
      }}
    >
      <strong>{badge.label}</strong> — {badge.description}
    </div>
  );
}
