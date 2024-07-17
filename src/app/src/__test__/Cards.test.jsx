import fetchData from "../components/cards/Cards";

jest.mock("../components/cards/Cards.jsx");

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
