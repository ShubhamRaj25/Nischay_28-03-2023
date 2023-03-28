import React from "react";
import "./buttonutility.css";

const Buttonutility = ({ text, width, height, textcolor, backgroundcolor }) => {
  return (
    <div>
      <button
        className="button_utility"
        style={{
          color: textcolor,
          background: backgroundcolor,
          width: width,
          height: height,
        }}
      >
        {text}
      </button>
    </div>
  );
};
export default Buttonutility;
