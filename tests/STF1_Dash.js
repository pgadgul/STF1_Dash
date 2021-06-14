import { Selector } from "testcafe";

fixture("Airport Gap Home Page").page(
  "https://airportgap-staging.dev-tester.com/"
);

test("Verify home page loads properly", async t => {
  const subtitle = Selector("h1").withText(
    "An API to fetch and save information about your favorite airports"
  );
  await t.expect(subtitle.exists).ok();
});