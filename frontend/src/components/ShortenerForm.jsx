import { useState } from "react";
import { shortenUrl } from "../services/api";

function ShortenerForm() {
  const [url, setUrl] = useState("");
  const [shortCode, setShortCode] = useState("");

  const handleSubmit = async (e) => {
    e.preventDefault();
    try {
      const data = await shortenUrl(url);
      setShortCode(data.short_code);
    } catch (error) {
      alert("Error connecting to backend");
      console.error(error);
    }
  };

  return (
    <div>
      <h2>URL Shortener</h2>
      <form onSubmit={handleSubmit}>
        <input
          value={url}
          onChange={(e) => setUrl(e.target.value)}
          placeholder="Enter URL"
        />
        <button type="submit">Shorten</button>
      </form>

      {shortCode && <p>Short Code: {shortCode}</p>}
    </div>
  );
}

export default ShortenerForm;