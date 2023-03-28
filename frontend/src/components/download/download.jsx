import React from "react";
import NavBar from "../../utilities/navbar/navbar";
import "./download.css";
import { useEffect } from "react";
import { getApi } from "../../callapi";
import { APIADDRESS } from "../../constants/constants";
import { useParams } from "react-router-dom";

const Downloadpage = () => {
  const params = useParams();
  var { radiovalue } = params;

  const headers1 = [
    "Lead Id",
    "Deal Id",
    "Customer Id",
    "Name",
    "Bank",
    "Account Number",
  ];
  const header2 = ["Action", "Count"];
  const header3 = ["Customer_Id", "Lead Id", "Deal Id", "Name"];
  const header4 = [
    "Document type",
    "Sub-type",
    "Identifier",
    "Name",
    "Customer-id/Name",
    "Allocated Customer_Id",
  ];
  useEffect(() => {
    getApi(APIADDRESS.DOWNLOAD1).then((response) => {
      console.log(response);
    });
  }, []);

  return (
    <div>
      <div>
        <NavBar radiovalue={radiovalue}></NavBar>
      </div>
      <div className="tables_downloadpage">
        <div className="table_downloadpage">
          <table className="table_fixed_download">
            <thead className="download_table_header">
              <tr>
                {headers1.map((item) => {
                  return <td key={item}>{item}</td>;
                })}
              </tr>
            </thead>
          </table>
        </div>
        <div className="table_downloadpage">
          <table className="table_fixed_download">
            <thead className="download_table_header">
              <tr>
                {header2.map((item) => {
                  return <td key={item}>{item}</td>;
                })}
              </tr>
            </thead>
          </table>
        </div>
        <div className="table_downloadpage">
          <table className="table_fixed_download">
            <thead className="download_table_header">
              <tr>
                {header3.map((item) => {
                  return <td key={item}>{item}</td>;
                })}
              </tr>
            </thead>
          </table>
        </div>
      </div>
      <div className="table_downloadpage">
        <table className="table_fixed_download">
          <thead className="download_table_header">
            <tr>
              {header4.map((item) => {
                return <td key={item}>{item}</td>;
              })}
            </tr>
          </thead>
        </table>
      </div>
    </div>
  );
};
export default Downloadpage;
