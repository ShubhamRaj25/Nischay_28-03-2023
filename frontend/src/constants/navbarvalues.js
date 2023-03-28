export const navBarValues = {
  HOME: " /images/home.png",
  UPLOAD: "/images/upload.png",
  DOWNLOAD: "/images/download.png",
  BUREAU: "/images/bureau.png",
  ANALYZE: "/images/analyze.png",
  SUMMARY: "/images/summary.png",
};

export const convertObjectIntoArrayOfObjects = (obj) => {
  let array = [];

  for (let x in obj) {
    array.push({ x: obj[x] });
  }

  return array;
};
