function PredictionCard({ prediction }) {
  if (!prediction) {
    return (
      <div className="mt-6 rounded-xl bg-white p-6 shadow-lg">
        <h2 className="mb-3 text-2xl font-bold">
          Prediction
        </h2>

        <p className="text-gray-500">
          No prediction yet.
        </p>
      </div>
    );
  }

  return (
    <div className="mt-6 rounded-xl bg-white p-6 shadow-lg">

      <h2 className="mb-4 text-2xl font-bold">
        Prediction
      </h2>

      <p className="text-xl font-semibold">
        {prediction.prediction === 1
          ? "✅ Survived"
          : "❌ Did Not Survive"}
      </p>

      <div className="mt-4 space-y-2">

        <p>
          <strong>Survival Probability:</strong>{" "}
          {(prediction.survived_probability * 100).toFixed(2)}%
        </p>

        <p>
          <strong>Death Probability:</strong>{" "}
          {(prediction.died_probability * 100).toFixed(2)}%
        </p>

      </div>

    </div>
  );
}

export default PredictionCard;