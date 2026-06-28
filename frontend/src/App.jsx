import { useState } from "react";

import PassengerForm from "./components/PassengerForm";
import PredictionCard from "./components/PredictionCard";

function App() {
  const [prediction, setPrediction] = useState(null);

  return (
    <main className="min-h-screen bg-gray-100 py-10">
      <div className="mx-auto max-w-xl">
        <h1 className="text-4xl font-bold text-center mb-8">
          Titanic Survival Predictor
        </h1>

        <PassengerForm setPrediction={setPrediction} />

        <PredictionCard prediction={prediction} />
      </div>
    </main>
  );
}

export default App;
