import { useState, useEffect } from 'react';

const Leaderboard = () => {
  const [leaderboard, setLeaderboard] = useState([]);

  useEffect(() => {
    fetch('http://localhost:5555/api/leaderboard')
      .then(response => response.json())
      .then(data => setLeaderboard(data.leaderboard));
  }, []);

  return (
    <div className="leaderboard">
      <h1>Leaderboard</h1>
      <table>
        <thead>
          <tr>
            <th>Rank</th>
            <th>Avatar</th>
            <th>User</th>
            <th>Total Points</th>
            <th>Badges</th>
          </tr>
        </thead>
        <tbody>
          {leaderboard.map((user, index) => (
            <tr key={user.user_id}>
              <td>{index + 1}</td>
              <td><img src={user.avatar_url} alt={user.username} /></td>
              <td>{user.username}</td>
              <td>{user.total_points}</td>
              <td>{user.badges.join(', ')}</td>
            </tr>
          ))}
        </tbody>
      </table>
    </div>
  );
};

export default Leaderboard;
