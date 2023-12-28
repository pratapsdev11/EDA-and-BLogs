class PCA:
  def __init__(self,num_components):
    self.num_components=num_components

  
  def standardize_data(self,x):
    self.mean= np.sum(x)/len(x)
    self.std= (sum((i-mean(x))**2 for i in x)/len(x))**0.5  
    std_data=x-mean(x)/std(x)
    return std_data
  def covariance(self,x):
    cov_mat=(self.standardize_data(x).T @ self.standardize_data(x))/(self.standardize_data(x).shape[0]-1)
    return cov_mat    
  def fit_n_transform(self,x):
    eig_vals,eig_vecs = np.linalg.eig(self.covariance(x))
    sort_idx=np.argsort(eig_vals)[::-1]
    eig_vals=eig_vals[sort_idx]
    eig_vecs=eig_vecs[:,sort_idx]
    self.components=eig_vecs[:self.num_components]
    explained_variance=np.sum(eig_vals[:self.num_components])/np.sum(eig_vals)
    print("component variance:\n",explained_variance)
    comp=self.components.T
    print("PCA:\n",np.dot(standardize_data(x),comp))