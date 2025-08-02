import { render, screen, fireEvent } from '@testing-library/react';
import { Button } from '../../components/Button';
import React from 'react';
test('chama onClick ao clicar', () => {
  const handleClick = jest.fn();
  render(<Button onClick={handleClick} />);
  fireEvent.click(screen.getByText('Clique'));
  expect(handleClick).toHaveBeenCalledTimes(1);
});
