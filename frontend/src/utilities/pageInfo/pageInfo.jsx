import React from "react";
import "./pageinfo.css";

const Pageinfo = ({ leadId, name }) => {
  return (
    <div className="pageinfo">
      <h4>
        Lead ID : {leadId} {name}
      </h4>
    </div>
  );
};
export default Pageinfo;
