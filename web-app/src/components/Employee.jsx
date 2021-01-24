import { useEffect, useState } from 'react'
import data from './assets/result.json'

const Employee = () => {

    const [results, setResults] = useState(null)

    useEffect((()=>{
        setResults(data.results)
    }))
    
    const renderData = () => {
        return(
            results.map((item)=>{
                return(
                    <div className="col-md-4">
                        <div className="result-card">
                            <p>
                                Applicant Name: <span>{item.name}</span>
                            </p>
                            <h5>
                                Match % : <span className={item.match>50?"green":"red"}>{item.match}%</span>
                            </h5>
                        </div>
                    </div>
                )
            })
        )
    }

    return(
        <div className="emp-details">
            <h1>Hey Parth Arora,<span> {results?results.length:null}</span> students asked for your referral !</h1>
            <div className="list">
                <div className="row">
                    {results?renderData():null}
                </div>
            </div>
        </div>
    )
}

export default Employee