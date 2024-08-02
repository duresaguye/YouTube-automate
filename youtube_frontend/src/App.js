import React, { useEffect, useState } from 'react';

function App() {
   const [podcasts, setPodcasts] = useState([]);

  useEffect(() => {
    const fetchPodcasts = async () => {
      try {
        const response = await fetch('http://localhost:8000/api/youtube/');
        const data = await response.json();
        setPodcasts(data);
      } catch (error) {
        console.error('Error fetching podcasts:', error);
      }
    };

    fetchPodcasts();
  }, []);

  return (
    <div className="p-4 mt-20">
      <h1 className="text-3xl font-bold mb-6">Podcasts</h1>
      <div className="grid grid-cols-1 sm:grid-cols-2 md:grid-cols-3 gap-6">
        {podcasts.map((podcast, index) => (
          <div key={index} className="bg-white shadow-md rounded-lg overflow-hidden">
            <div className="relative">
              <iframe
                width="100%"
                height="315"
                src={podcast.embed_url}
                title={`Podcast Video ${index}`}
                frameBorder="0"
                allowFullScreen
                className="w-full h-48 object-cover"
              ></iframe>
            </div>
            <div className="p-4">
              <h2 className="text-xl font-semibold mb-2">Podcast Video {index + 1}</h2>
              <p className="text-gray-600 mb-4">No additional data available</p>
            </div>
          </div>
        ))}
      </div>
    </div>
  );
};


export default App;
