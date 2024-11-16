import React from 'react';

const Leaderboard = ({ players = [
  { rank: 1, name: "Sarah Smith", score: 2500, avatar: "S" },
  { rank: 2, name: "John Doe", score: 2300, avatar: "J" },
  { rank: 3, name: "Mike Johnson", score: 2100, avatar: "M" },
  { rank: 4, name: "Emily Brown", score: 1900, avatar: "E" },
  { rank: 5, name: "Chris Wilson", score: 1800, avatar: "C" }
] }) => {
  return (
    <div className="bg-white rounded-lg shadow-md p-6 max-w-2xl mx-auto">
      <h2 className="text-2xl font-bold mb-4 text-center">Leaderboard</h2>
      
      <div className="space-y-4">
        {players.map((player) => (
          <div 
            key={player.rank}
            className="flex items-center justify-between p-3 bg-gray-50 rounded-lg hover:bg-gray-100 transition-colors"
          >
            <div className="flex items-center space-x-4">
              <span className={`
                w-8 h-8 flex items-center justify-center rounded-full
                ${player.rank === 1 ? 'bg-yellow-400' :
                  player.rank === 2 ? 'bg-gray-300' :
                  player.rank === 3 ? 'bg-orange-400' : 'bg-blue-400'}
                text-white font-bold
              `}>
                {player.rank}
              </span>
              <div className="w-10 h-10 bg-blue-500 rounded-full flex items-center justify-center">
                <span className="text-white font-bold">{player.avatar}</span>
              </div>
              <span className="font-semibold">{player.name}</span>
            </div>
            <div className="flex items-center space-x-2">
              <span className="font-bold">{player.score}</span>
              <span className="text-sm text-gray-500">XP</span>
            </div>
          </div>
        ))}
      </div>
    </div>
  );
};

export default Leaderboard;