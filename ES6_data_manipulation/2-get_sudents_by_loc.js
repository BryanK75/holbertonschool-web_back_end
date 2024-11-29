/*eslint-disable*/
export default function getStudentsByLocation(objects_array, location) {
  if (!Array.isArray(objects_array)) return [];
  return objects_array.filter((object) => object.location === location);
}
