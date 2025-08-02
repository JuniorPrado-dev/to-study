# Setup to make tests with jest
## install packages
``` bash
npm install --save-dev jest @testing-library/react @testing-library/jest-dom @testing-library/user-event babel-jest jest-environment-jsdom
```
## Babel config
- make file babel.config.cjs and put:
``` 
module.exports = {
  presets: ['@babel/preset-env', '@babel/preset-react'],
};
```
Obs: If in this project uses EsLint add in eslint.config:
``` 
module.exports = {
  env: {
    browser: true,
    es2021: true,
    jest: true,
    node: true, // 👈 ESSENCIAL para reconhecer "module", "require", etc.
  },
  // resto da config...
};
```
## Add Jest.config
- make file jest.config.cjs and put:
``` 
module.exports = {
  testEnvironment: 'jsdom',
  setupFilesAfterEnv: ['./src/setupTests.js'],
  moduleNameMapper: {
    '^@/(.*)$': '<rootDir>/src/$1', // se usar alias como @/
    '\\.(css|scss|sass)$': 'identity-obj-proxy',
  },
  transform: {
    '^.+\\.(js|jsx|ts|tsx)$': 'babel-jest',
  },
};
```
## Add setupTests
- make file setupTests.js in /src and put:
``` 
import '@testing-library/jest-dom';
```
## Add script
- add in your package.json:
``` json
"scripts": {
  "test": "jest"
}

```
## Run test
``` bash
npm test or npm run test
```
