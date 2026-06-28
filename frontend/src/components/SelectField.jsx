function SelectField({ label, name, options, value, onChange }) {
  return (
    <div className="flex flex-col gap-2">
      <label htmlFor={name} className="font-medium text-gray-700">
        {label}
      </label>

      <select
        id={name}
        name={name}
        value={value}
        onChange={onChange}
        className="
          w-full
          rounded-lg
          border
          border-gray-300
          p-3
          focus:outline-none
          focus:ring-2
          focus:ring-blue-500
        "
      >
        {options.map((option) => (
          <option key={option.value} value={option.value}>
            {option.label}
          </option>
        ))}
      </select>
    </div>
  );
}

export default SelectField;
