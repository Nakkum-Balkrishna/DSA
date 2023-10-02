const asyncFun = async (a, b) => {
  return new Promise((resolve, reject) => {
    if (a === undefined || b === undefined) {
      reject("Please provide proper values to add.");
    }
    setTimeout(() => {
      const res = a + b;
      resolve(res);
    }, 2000);
    // reject("This is some custom error")
  });
};

// This is the example of callback hell.
asyncFun(2, 3)
  .then((result) => {
    console.log("First result is :", result);
    asyncFun(result, 5)
      .then((result) => {
        console.log("second result is :", result);
        asyncFun(result, ) // this should throw error.
          .then((result) => {
            console.log("Final result is :", result);
          })
          .catch((error) => {
            console.log(error);
          });
      })
      .catch((error) => {
        console.log(error);
      });
  })
  .catch((error) => {
    console.log(error);
  });
