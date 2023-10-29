/**
 * Different types of testing.
 * 1. Manual Testing
 * 2. Automation Testing 
 *      i. Selenium Testing
 * 3. End to End (E2E) testing : Covers entire user journey
 * 4. Unit Testing
 * 5. Integration Testing
 * 
 */

/**
 *  1. Install React Testing library(browse this keyword)
 *  2. Instal Jest
 *  3. Configure Jest(use npx to configure)
 *  4. Install jest-environment-jsdom
 *  5. Create first test case
 *  6. Create a folder with name "--tests__"  
 *  7. Create the test cases
 *  8. Install babel (npm install babel-jest/@bebel/core and @babel/preset-env)
 *  9. Configure the babel
 *  
 */

//test case 1:
export const sum = (a, b) => a+b;

//test case:
test("Check the sum of the 2 positive numbers", () => {
    expect(sum(2, 5)).toBe(7);
})

// test case 2:
import Header from "../header"
import {Provider} from "react-dom" 
import store from "../util/store"
import {StaticRouter} from "react-router-dom/server"
test("logo should load on rendering header", () => {
    //load the header
    const header = render(
        <StaticRouter>
            <Provider store={store}>
                <Header/>
            </Provider>
        </StaticRouter>
    //error : js doesnt understand jsx
    //need to install babel(@babel/preset-reset)
    );

    const logo = header.getAllByTestId("logo"); // return an array
    // need to write his test id in the code as below
    // <img data-testid="logo" >
    expect(logo[0].src).toBe("dummyLogo.png");
    
    //check if the logo is loaded
})


//test case 3:
import Header from "../header"
import {Provider} from "react-dom" 
import store from "../util/store"
import {StaticRouter} from "react-router-dom/server"
test("Online status should be green on rendering the header.", () => {
    const header = render(
        <StaticRouter>
            <Provider store={store}>
                <Header/>
            </Provider>
        </StaticRouter>
    );

    const OnlineStatus = header.getAllByTestId("online-status"); // return an array
    expect(OnlineStatus.innerHTML).toBe("GreenTickEmoji");
})