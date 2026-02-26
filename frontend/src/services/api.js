// Inside api.js
export const shortenUrl = async (inputUrl) => {
  const response = await fetch('http://localhost:5000/api/shorten', {
    method: 'POST',
    headers: {
      'Content-Type': 'application/json',
    },
    // Ensure the key is "long_url" to match Flask!
    body: JSON.stringify({ long_url: inputUrl }), 
  });
  
  if (!response.ok) {
    throw new Error('Network response was not ok');
  }
  return response.json();
};