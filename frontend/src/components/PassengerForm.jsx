import { useState } from "react";

import InputField from "./InputField";
import SelectField from "./SelectField";
import { predictPassenger } from "../services/api";

function PassengerForm({ setPrediction }) {
  const [formData, setFormData] = useState({
    pclass: 1,
    sex: "male",
    age: "",
    sibsp: 0,
    parch: 0,
    fare: "",
    embarked: "S",
  });

  const handleSubmit = async (event) => {
    event.preventDefault();
    // console.log(formData);
    
    try {
      const result = await predictPassenger(formData);
      setPrediction(result);

      // console.log(result);
    } catch (error) {
      console.error(error);
    }
  };

  const handleChange = (event) => {
  const { name, value } = event.target;

  const numericFields = [
    "pclass",
    "age",
    "sibsp",
    "parch",
    "fare",
  ];

  setFormData((prevData) => ({
    ...prevData,
    [name]: numericFields.includes(name)
      ? Number(value)
      : value,
  }));
};

  return (
    <form
      className="bg-white rounded-xl shadow-lg p-6 space-y-5"
      onSubmit={handleSubmit}
    >
      <h2 className="text-2xl font-bold">Passenger Information</h2>

      <SelectField
        label="Passenger Class"
        name="pclass"
        options={[
          { value: 1, label: "First Class" },
          { value: 2, label: "Second Class" },
          { value: 3, label: "Third Class" },
        ]}
        value={formData.pclass}
        onChange={handleChange}
      />

      <SelectField
        label="Sex"
        name="sex"
        options={[
          { value: "male", label: "Male" },
          { value: "female", label: "Female" },
        ]}
        value={formData.sex}
        onChange={handleChange}
      />

      <InputField
        label="Age"
        name="age"
        type="number"
        placeholder="Enter age"
        value={formData.age}
        onChange={handleChange}
      />

      <InputField
        label="Fare"
        name="fare"
        type="number"
        placeholder="Enter fare amount"
        value={formData.fare}
        onChange={handleChange}
      />

      <InputField
        label="Siblings/Spouses"
        name="sibsp"
        type="number"
        placeholder="Enter value"
        value={formData.sibsp}
        onChange={handleChange}
      />

      <InputField
        label="Parents/Children"
        name="parch"
        type="number"
        placeholder="Enter value"
        value={formData.parch}
        onChange={handleChange}
      />

      <SelectField
        label="Embarked"
        name="embarked"
        options={[
          { value: "C", label: "Cherbourg" },
          { value: "Q", label: "Queenstown" },
          { value: "S", label: "Southampton" },
        ]}
        value={formData.embarked}
        onChange={handleChange}
      />

      {/* <pre>{JSON.stringify(formData, null, 2)}</pre> */}
      <button
        type="submit"
        className="
        w-full
        bg-blue-600
        hover:bg-blue-700
        text-white
        font-semibold
        py-3
        rounded-lg
        transition
    "
      >
        Predict
      </button>
    </form>
  );
}

export default PassengerForm;
