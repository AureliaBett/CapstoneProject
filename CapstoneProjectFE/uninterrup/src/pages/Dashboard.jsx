import { useEffect, useState } from "react";
import { getUPSUnits } from "../api/upsApi";

const Dashboard = () => {
  const [upsList, setUpsList] = useState([]);
  const [loading, setLoading] = useState(true);

  useEffect(() => {
    getUPSUnits().then(data => {
      console.log("DATA FROM API:", data);
      setUpsList(data);
      setLoading(false);
    });
  }, []);

  if (loading) return <p>Loading...</p>;

  return (
    <div className="p-6">
      <h1 className="text-xl font-bold mb-4">UPS Units</h1>

      <div className="grid grid-cols-1 md:grid-cols-3 gap-4">
        {upsList.map(ups => (
          <div key={ups.id} className="p-4 bg-black shadow rounded">
            <p><b>Model:</b> {ups.model}</p>
            <p><b>Serial:</b> {ups.serial_number}</p>
            <p><b>Status:</b> {ups.status}</p>
            <p><b>Client:</b> {ups.status}</p>
          </div>
        ))}
      </div>
    </div>
  );
};

export default Dashboard;
