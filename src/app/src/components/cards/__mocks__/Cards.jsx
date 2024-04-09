const fetchData = jest.fn(() => {
  return Promise.resolve({
    "page_number": "",
    "num_of_objects": 0,
    "data": [{}]
  });
});

export default fetchData;
