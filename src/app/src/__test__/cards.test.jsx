import jest from "jest";
jest.mock("./card.scss", () => {
  return {};
});

import {fetchData} from "../components/cards/Cards";

jest.mock("../__mocks__/Cards.jsx");

describe("cards", () => {
  it("gets the the game(s) information", async () => {
    expect.hasAssertions();
    //Arrange


    //Act
    const data = await fetchData();

    //Assert

    expect(data.num_of_objects).toBe(0);
  });
});
