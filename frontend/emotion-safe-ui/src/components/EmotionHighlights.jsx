export default function EmotionHighlights({ text, highlights }) {
  if (!highlights || highlights.length === 0) return <p>No manipulative phrases detected.</p>;

  let result = [];
  let lastIndex = 0;

  highlights.forEach((h, i) => {
    result.push(text.slice(lastIndex, h.start));
    result.push(
      <span key={i} style={{backgroundColor: "#fde68a",padding: "0 4px",borderRadius: "4px",fontWeight: 600,}}>
        {text.slice(h.start, h.end)}
      </span>
    );
    lastIndex = h.end;
  });

  result.push(text.slice(lastIndex));

  return (
    <div>
      <h3>Highlighted Text</h3>
      <p>{result}</p>
    </div>
  );
}
