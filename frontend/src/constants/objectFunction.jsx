export const objectFunction = (backendobject) => {
  let response = [];

  for (let data of backendobject.data) {
    var localobject = {};
    for (let keyindex in backendobject.columns) {
      for (let valueindex in data) {
        if ((keyindex = valueindex)) {
          let keyvalue = backendobject.columns[keyindex];
          let valuepair = data[valueindex];
          localobject[keyvalue] = valuepair;
        }
      }
    }
    response.push(localobject);
  }
  return response;
};
