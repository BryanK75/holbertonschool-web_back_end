/*eslint-disable*/
export default function createInt8TypeArray(lenght, position, value) {
  const buffer = new ArrayBuffer(lenght);
  const view = new DataView(buffer);
  if (position > lenght - 1) {
    throw new Error('Position outside range');
  }
  view.setInt8(position, value);
  return view;
}
