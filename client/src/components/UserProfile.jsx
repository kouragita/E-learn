import React from 'react';

const UserProfile = ({ user = {
  name: "John Doe",
  level: 5,
  xp: 2500,
  totalXp: 3000,
  achievements: ["First Login", "Profile Complete", "Win Streak"]
} }) => {
  return (
    <div className="bg-white rounded-lg shadow-md p-6 max-w-sm mx-auto">
      <div className="flex items-center space-x-4">
        <div className="w-16 h-16 bg-blue-500 rounded-full flex items-center justify-center">
          <span className="text-2xl text-white">{user.name[0]}</span>
        </div>
        <div>
          <h2 className="text-xl font-bold">{user.name}</h2>
          <p className="text-gray-600">Level {user.level}</p>
        </div>
      </div>
      
      <div className="mt-4">
        <div className="mb-2">
          <div className="flex justify-between text-sm">
            <span>XP Progress</span>
            <span>{user.xp} / {user.totalXp}</span>
          </div>
          <div className="w-full bg-gray-200 rounded-full h-2.5">
            <div 
              className="bg-blue-600 h-2.5 rounded-full" 
              style={{ width: `${(user.xp / user.totalXp) * 100}%` }}
            ></div>
          </div>
        </div>
      </div>

      <div className="mt-4">
        <h3 className="font-semibold mb-2">Achievements</h3>
        <div className="space-y-2">
          {user.achievements.map((achievement, index) => (
            <div key={index} className="flex items-center space-x-2">
              <span className="text-yellow-500">🏆</span>
              <span>{achievement}</span>
            </div>
          ))}
        </div>
      </div>
    </div>
  );
};

export default UserProfile;