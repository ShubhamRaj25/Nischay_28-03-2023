import React from "react";
import { makeStyles } from "@material-ui/core/styles";
import Button from "@material-ui/core/Button";
import { BiArrowToTop } from "react-icons/bi";

const useStyles = makeStyles((theme) => ({
  root: {
    position: "fixed",
    bottom: theme.spacing(2),
    right: theme.spacing(2),
  },
}));

const ScrollToTop = () => {
  const classes = useStyles();

  const handleClick = () => {
    window.scrollTo({
      top: 0,
      left: 0,
      behavior: "smooth",
    });
  };

  return (
    <Button onClick={handleClick} className={classes.root}>
      <BiArrowToTop size={30}></BiArrowToTop>
    </Button>
  );
};

export default ScrollToTop;
