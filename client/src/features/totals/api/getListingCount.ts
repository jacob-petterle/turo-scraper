

export const getListingCount = (): Promise<number> => {
  return axios.get(`/count`);
}