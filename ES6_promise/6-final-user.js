/* eslint-disable */
import signUpUser from './4-user-promise';
import uploadPhoto from './5-photo-reject';

export default async (firstName, lastName, fileName) => {
  const results = await Promise.allSettled([signUpUser(firstName, lastName), uploadPhoto(fileName)]);
  return results.map((promise) => ({
    status: promise.status,
    value: promise.status === 'fulfilled' ? promise.value : `${promise.reason.name}: ${promise.reason.message}`,
  }));
};
