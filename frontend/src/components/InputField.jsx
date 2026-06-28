function InputField({ label, type = "text", placeholder, name, value, onChange }) {
  return (
    <div className="flex flex-col gap-2">
      <label htmlFor={name} className="font-medium text-gray-700">
        {label}
      </label>

      <input
        id={name}
        name={name}
        type={type}
        placeholder={placeholder}
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
      />
    </div>
  );
}

export default InputField;
