/*eslint-disable*/
export default function updateStudentGradeByCity(students_array, city, newGrade) {
  return students_array
    .filter((student) => student.location === city)
    .map((student) => {
        const grade = newGrade.filter((newGrade) => newGrade.studentId === student.id)[0];
        student.grade = grade ? grade.grade : 'N/A';
        return student;
  });
}
